import whisper
import time

# models: "base", "base.en", "tiny.en"
model = whisper.load_model("tiny.en")

start_time = time.time()
result = model.transcribe("data\input.mp3")
end_time = time.time()

print(result["text"])
difference = end_time - start_time
print(f"Tempo de processamento: {difference:.2f} segundos")
