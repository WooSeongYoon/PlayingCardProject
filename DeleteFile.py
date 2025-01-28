import os
def DeleteAllFile(Folder):
    for filename in os.listdir(Folder):
        file_path = os.path.join(Folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
