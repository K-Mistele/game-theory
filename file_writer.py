import json as JSON

# class for writing to/from files for communication between AI's
class file_writer:
    def __init__(self, fname):
        self.file = open("fname", "w+") # read and write

    def __repr__(self):
        return self.file
        #TODO: code to return all data in document so far

    #method for encoding Python data to JSON
    def encode_json(self, to_encode):
        json_string = JSON.dumps(to_encode)
        return json_string

    #method for decoding JSON to Python
    def decode_json(self, to_decode):
        python_data = JSON.loads(to_decode)
        return python_data

    #method for writing to file
    def write_to_file(self, to_write, want_encoded=False):
        if want_encoded == True:
            self.file.write(self.encode_json(to_write))
        else:
            self.file.write(to_write)

    #method for getting last line of file
    def read_last_line(self, want_decoded=False):
        all_lines = self.file.readlines()
        if want_decoded == True:
            last_line = self.decode_json(all_lines[len(all_lines)-1])
            return last_line
        else:
            last_line = all_lines[len(all_lines)-1]
            return last_line

