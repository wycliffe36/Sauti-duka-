import noisereduce as nr
import soundfile as sf

def clean_audio(input_path, output_path):
    # Read the noisy shop audio
    data, rate = sf.read(input_path)
    # Remove background noise
    reduced = nr.reduce_noise(y=data, sr=rate)
    # Save clean version
    sf.write(output_path, reduced, rate)
    return output_path
