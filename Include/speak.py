'''
this example is use's gTTS (google text-to-Speech) and
SpeechRecognition v3.8.1
and PyAudio
'''

# only using google ?

from google.cloud import speech_v1p1beta1 as speech

def sample_recognition(storage_uri, phrase):
    '''
    transcribe a short audio file with speech-SpeechRecognition
    '''
    client = speech.SpecchClient()

    phrase = [phrase]

    boost = 20.0
    speech_contexts_element = {"phrase": phrase, "boost": boost}
    speech_contexts = [speech_contexts_element]

    # sample rate in hertz of the audio data sent
    sample_rate_hertz = 44100

    # the language
    language_code = "en_AU"

    encoding = speech.RecognitionConfig.AudioEncoding.MP3

    config = {
    "speech_contexts": speech_contexts,
    "sample_rate_hertz": sample_rate_hertz,
    "language_code": language_code,
    "encoding": encoding
    }

    audio = {"uri": storage_uri}

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        # first alternative is the most probable result
        alternative = result.alternative[0]
        print(u"Transcribe: {}".format(alternative.transcript))

print('all goood')
