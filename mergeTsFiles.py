import os
import ffmpy3

## ffmpeg command
# ffmpeg -i "concat:0.ts|1.ts" -c copy "output/1.mp4"
# ffmpeg -i "concat:0.ts|1.ts" -c copy "1.mp4"

def generate_input_file(original_path, generated_input_file_name):
    file = open(generated_input_file_name, "w", encoding='utf-8')

    ts_files_count = len(os.listdir(original_path))
    count = 0
    while(count < ts_files_count):
        file.write("file '{}/{}.ts'".format(original_path, count))

        if((count+1) != ts_files_count):
            file.write('\n')

        count+=1
    
    file.close()
    os.chmod(generated_input_file_name, 0o666)

def generate_input_file2(original_path, generated_input_file_name):
    count = 0
    ts_files_count = len(os.listdir(original_path))
    
    with open(generated_input_file_name, "w", encoding='utf-8') as file:
        while(count < ts_files_count):
            file.write("file '{}/{}.ts'".format(original_path, count))

            if((count+1) != ts_files_count):
                file.write('\n')

            count+=1

    os.chmod(generated_input_file_name, 0o666)    

generated_input_file_name = "input.txt"
generated_output_file_name = "test.mp4"
original_path = "TSFiles" # put all TS files to this folder
generate_input_file2(original_path, generated_input_file_name)

# FFmpeg -f concat -i file.txt -c copy FileName.mp4
ff = ffmpy3.FFmpeg(inputs = {generated_input_file_name: '-f concat'}, outputs = {generated_output_file_name: '-c copy'})
ff.run()

 
