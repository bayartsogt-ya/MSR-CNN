from pydub import AudioSegment
from pydub.silence import split_on_silence

def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)


def get_chunk(filename):

    song = AudioSegment.from_file("uploads/original/"+str(filename), format='webm', codec='libopus')

    #split track where silence is 2 seconds or more and get chunks
    silence_thresh = 15
    chunks = []
    while len(chunks) < 1 and silence_thresh < 60:
        chunks = split_on_silence(song, 
            # must be silent for at least 2 seconds or 2000 ms
            min_silence_len=2500,

            # consider it silent if quieter than -16 dBFS
            #Adjust this per requirement
            silence_thresh=-silence_thresh
        )
        
        silence_thresh += 1
        
    if( len(chunks) == 0 ):
        return "silence"
    chunk = chunks[0]
    chunk.frame_rate = 44100
    #Create 0.5 seconds silence chunk
    duration = (1000 - len(chunk))/2

    if len(chunk)<=1000:
        silence_chunk = AudioSegment.silent(duration=duration)
        chunk = silence_chunk + chunk + silence_chunk
    else:
        chunk = chunk[:(len(chunk)+duration)]
        chunk = chunk[-(len(chunk)+duration):]
    
    #Normalize each audio chunk
    normalized_chunk = match_target_amplitude(chunk, -20.0)
    #Export audio chunk with new bitrate
    normalized_chunk.export(".//uploads/chunk0.wav", bitrate='192k', format="wav")
