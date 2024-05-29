import ffmpeg
import os

def convert_audio(input_file, output_format='wav'):
    # Check if the file exists
    if not os.path.exists(input_file):
        print(f"The file {input_file} does not exist.")
        return
    
    # Define the output file name based on the new format
    output_file = os.path.splitext(input_file)[0] + f'.{output_format}'
    
    # Run the conversion
    ffmpeg.input(input_file).output(output_file).run()
    print(f"Converted {input_file} to {output_file}")

def main():
    # Get user input for file paths
    file_paths = input("Please enter the paths to your audio files, separated by commas: ")
    files = file_paths.split(',')

    # Optional: Ask for output format
    output_format = input("Please enter the desired output format (default is WAV): ").strip()
    if not output_format:
        output_format = 'wav'
    
    # Process each file
    for file_path in files:
        file_path = file_path.strip()  # Clean up any extra spaces
        convert_audio(file_path, output_format)

if __name__ == '__main__':
    main()

