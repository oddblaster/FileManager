import os



downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
pictures_path = os.path.join(os.path.expanduser('~'), 'Pictures')
music_path = os.path.join(os.path.expanduser('~'), 'Music')
video_path = os.path.join(os.path.expanduser('~'), 'Videos')


#Retrieves the file type
def get_file_type(filename):
    _, extension = os.path.splitext(filename)
    return extension

#Moves the file to the specific folder
def move_file(file, path):
    
    src_path = os.path.join(downloads_path, file)
    dst_path = os.path.join(path, file)
    if(src_path != dst_path):
        os.rename(src_path, dst_path)


if __name__ == "__main__":
    for file in os.listdir(downloads_path):
        file_type = get_file_type(file)
        
        if(file_type == ".pdf" or
           file_type == ".docx"):
            move_file(file,documents_path)
        elif(file_type == ".png" or
             file_type == ".gif" or
             file_type == ".jpeg" or
             file_type == ".tiff" or
             file_type == ".svg" or
             file_type == ".webp"):

            move_file(file,pictures_path)

        elif(file_type == ".webm" or
             file_type == ".mkv" or
             file_type == ".flv" or
             file_type == ".vob" or
             file_type == ".mp4"):

            move_file(file,video_path)

        elif(file_type == ".mp3"):
            move_file(file,video_path)
        

        
