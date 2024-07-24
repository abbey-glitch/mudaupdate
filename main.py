# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# class MyHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         print(f'File {event.src_path} has been modified')

#     def on_created(self, event):
#         print(f'File {event.src_path} has been created')

#     def on_deleted(self, event):
#         print(f'File {event.src_path} has been deleted')

# if __name__ == "__main__":
#     event_handler = MyHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path='.', recursive=True)
#     observer.start()

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()

import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class TestRunnerHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            self.run_tests()

    def run_tests(self):
        try:
            result = subprocess.run(['pytest'], check=False, capture_output=True, text=True)
            print(result.stdout)
            print(result.stderr)
            if result.returncode == 0:
                print("Tests passed successfully.")
            else:
                print("Some tests failed.")
        except subprocess.CalledProcessError as e:
            print(f"Error running tests: {e}")

if __name__ == "__main__":
    path = "."  # Directory to watch
    event_handler = TestRunnerHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    observer.start()
    print(f"Watching for changes in {path}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()