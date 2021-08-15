# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from ovos_plugin_manager.templates.hotwords import HotWordEngine
from ovos_utils.log import LOG
from os.path import join, isfile, expanduser, dirname
from petact import install_package
from xdg import BaseDirectory as XDG
from precise_lite_runner import PreciseRunner, PreciseEngine, ReadWriteStream
import precise_lite


class PreciseLiteHotwordPlugin(HotWordEngine):
    """Precise is the default wake word engine for Mycroft.
    This is the community developed TfLite version of that engine
    """
    def __init__(self, key_phrase="hey mycroft", config=None, lang="en-us"):
        super().__init__(key_phrase, config, lang)
        self.expected_duration = self.config.get("expected_duration") or 3
        self.has_found = False
        self.stream = ReadWriteStream()

        self.trigger_level = self.config.get('trigger_level', 3)
        self.sensitivity = self.config.get('sensitivity', 0.5)

        model = self.config.get('model')
        if model and model.startswith("http"):
            model = self.download_model(model)

        if not model or not isfile(expanduser(model)):
            raise ValueError("Model not found")

        self.precise_model = expanduser(model)

        precise_exe = join(dirname(precise_lite.__file__),
                           "scripts", "engine.py")
        self.runner = PreciseRunner(
            PreciseEngine(precise_exe, self.precise_model),
            self.trigger_level, self.sensitivity,
            stream=self.stream, on_activation=self.on_activation,
        )
        self.runner.start()

    @staticmethod
    def download_model(url):
        name = url.split("/")[-1].split(".")[0] + ".tflite"
        folder = join(XDG.xdg_data_home, "precise-lite")
        model_path = join(folder, name)
        if not isfile(model_path):
            LOG.info("Downloading model for precise-lite:")
            LOG.info(url)
            install_package(url, folder)
            LOG.info(f"Model downloaded to {model_path}")

        return model_path

    def on_activation(self):
        self.has_found = True

    def update(self, chunk):
        self.stream.write(chunk)

    def found_wake_word(self, frame_data):
        if self.has_found:
            self.has_found = False
            return True
        return False

    def stop(self):
        if self.runner:
            self.runner.stop()
