
import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk



def speak_to_microphone (api_key, region):

    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)
    speech_config.speech_recognition_language = "en-US"
    audio_config = speechsdk.audio.AudioConfig(device_name='{0.0.1.00000000}.{21F68B62-5124-4427-9D6A-CE11E415922E}')
    speech_recognizer = speechsdk. SpeechRecognizer (speech_config=speech_config, audio_config=audio_config)

    # Set timeout durations
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "60000")
    speech_recognizer.properties.set_property(speechsdk.PropertyId. SpeechServiceConnection_EndSilenceTimeoutMs, "20000")
    print("Speak into your microphone. Say 'stop session' to end.")

    while True:

        speech_recognition_result = speech_recognizer.recognize_once_async().get()
        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:

            print("Recognized: {}".format(speech_recognition_result.text))

            if "stop session" in speech_recognition_result.text.lower():
                print("Session ended by user.")
                break
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch :
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled :
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details. reason == speechsdk.CancellationReason.Error :
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

api_key = os.getenv("api_key")
region = os.getenv("region")

speak_to_microphone (api_key, region)

