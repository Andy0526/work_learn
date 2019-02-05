import io
from google.cloud import speech_v1p1beta1 as speech
client = speech.SpeechClient()

speech_file = 'resources/commercial_mono.wav'

with io.open(speech_file, 'rb') as audio_file:
    content = audio_file.read()

audio = speech.types.RecognitionAudio(content=content)
config = speech.types.RecognitionConfig(
    encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    language_code='en-US',
    # Enhanced models are only available to projects that
    # opt in for audio data collection.
    use_enhanced=True,
    # A model must be specified to use enhanced model.
    model='phone_call')

response = client.recognize(config, audio)

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print('-' * 20)
    print('First alternative of result {}'.format(i))
    print('Transcript: {}'.format(alternative.transcript))