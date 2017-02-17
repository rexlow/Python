import cmu_sphinx4
audio_url = 'http://audio.com/audio.wav'
transcriber = cmu_sphinx4.Transcriber(audio_url)
for line in transcriber.transcript_stream():
    print line
