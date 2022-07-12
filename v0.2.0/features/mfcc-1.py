from spafe.features.mfcc import mel_spectrogram
from spafe.utils.vis import show_spectrogram
from scipy.io.wavfile import read

# read audio
fpath = "../../../test.wav"
fs, sig = read(fpath)

mSpec, _ = mel_spectrogram(sig,
                                fs=fs,
                                pre_emph=0,
                                pre_emph_coeff=0.97,
                                win_len=0.030,
                                win_hop=0.015,
                                win_type="hamming",
                                nfilts=128,
                                nfft=2048,
                                low_freq=0,
                                high_freq=fs/2)


show_spectrogram(mSpec.T,
                 fs,
                 xmin=0,
                 xmax=len(sig)/fs,
                 ymin=0,
                 ymax=(fs/2)/1000,
                 dbf=80.0,
                 xlabel="Time (s)",
                 ylabel="Frequency (kHz)",
                 title="Mel spectrogram (dB)",
                 cmap="jet")