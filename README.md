## Description

OpenVoiceOS wake word plugin for [precise-lite](https://github.com/OpenVoiceOS/precise-lite)

train models with [precise-lite-trainer](https://github.com/OpenVoiceOS/precise-lite-trainer) or download pre-trained [precise-lite-models](https://github.com/OpenVoiceOS/precise-lite-models)

## Install

This package supports both tflite-runner and the full tensorflow.

To install with tflite, use `pip install ovos-ww-plugin-precise-lite[tflite]`.
For the full tensorflow use `pip install ovos-ww-plugin-precise-lite[full]`.

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

Get community models [here](https://github.com/OpenVoiceOS/precise-lite-models)

## Other Programming Languages

Community members have ported precise to other programming languages
- Go - [precise-go](https://github.com/tystuyfzand/precise-go) by [tystuyfzand](https://github.com/tystuyfzand)
- Rust - [precise-rs](https://github.com/sheosi/precise-rs) by [sheosi](https://github.com/sheosi)
