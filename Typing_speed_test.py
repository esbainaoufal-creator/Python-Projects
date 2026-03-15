import time

sentence = "The quick brown fox jumps over the lazy dog"
word_count = len(sentence.split())

print("=" * 50)
print("         TYPING SPEED TEST")
print("=" * 50)
print()

while True:
    input("  Press Enter to start...")
    print()
    print("-" * 50)
    print(f"  {sentence}")
    print("-" * 50)
    print()
    start = time.time()
    typed = input("  > ")
    end = time.time()

    elapsed = end - start
    wpm = word_count / (elapsed / 60)

    matched = 0
    for char1, char2 in zip(sentence, typed):
        if char1 == char2:
            matched += 1

    accuracy = (matched / len(sentence)) * 100

    print()
    print("=" * 50)
    print("         RESULTS")
    print("=" * 50)
    print(f"  WPM      : {int(wpm)}")
    print(f"  Accuracy : {round(accuracy, 1)}%")
    print(f"  Time     : {round(elapsed, 2)}s")
    print("=" * 50)
    
    choice = input("You wanna start again? (y or n)")
    if choice == "y" or choice == "":
        continue
    else:
        break
