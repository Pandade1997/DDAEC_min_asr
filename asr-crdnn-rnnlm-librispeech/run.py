from speechbrain.pretrained import EncoderDecoderASR

asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-rnnlm-librispeech",
                                           savedir="pretrained_models/asr-crdnn-rnnlm-librispeech")
temp = asr_model.transcribe_file('speechbrain/asr-crdnn-rnnlm-librispeech/example.wav')

print('11111111111')
