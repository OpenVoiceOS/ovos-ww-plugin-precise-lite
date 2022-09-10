## Description
Mycroft wake word plugin for [precise-lite](https://alphacephei.com/vosk/)

## Install

`pip install ovos-ww-plugin-precise-lite`

## Configuration

Add the following to your hotwords section in mycroft.conf 

```json
"listener": {
  "wake_word": "hey mycroft"
},
"hotwords": {
  "hey mycroft": {
    "module": "ovos-ww-plugin-precise-lite",
    "model": "https://github.com/OpenVoiceOS/precise-lite-models/raw/master/wakewords/en/hey_mycroft.tflite",
    "listen": true,
    "sound": "snd/start_listening.wav",
    "expected_duration": 3,
    "trigger_level": 3,
    "sensitivity": 0.5
   }
}
```