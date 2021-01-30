from google.cloud import texttospeech


class GoogleAudioManager:

    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()

    def fetch_audio(self, text, output_file_name):
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-GB",
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        with open(f"audio-files/{output_file_name}.mp3", "wb") as out:
            out.write(response.audio_content)
            print(f'Audio content written to file {output_file_name}')
            return True

    def text_to_speech(self, text, outfile):

        ssml = "<speak>{}</speak>".format(
            text.replace("\n", '\n<break time="2s"/>')
        )

        synthesis_input = texttospeech.SynthesisInput(ssml=ssml)

        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        request = texttospeech.SynthesizeSpeechRequest(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        response = self.client.synthesize_speech(request=request)

        with open(outfile, "wb") as out:
            out.write(response.audio_content)
            print("Audio content written to file " + outfile)