"""
Unit tests for emotion detection application.
"""
from EmotionDetection import emotion_detector


def test_emotion_detector():
    """
    Test emotion detector with different text inputs.
    """
    # Test case 1: Joy
    result = emotion_detector("I am glad this happened")
    assert result['dominant_emotion'] == 'joy', f"Expected 'joy', got {result['dominant_emotion']}"
    
    # Test case 2: Anger
    result = emotion_detector("I am really mad about this")
    assert result['dominant_emotion'] == 'anger', f"Expected 'anger', got {result['dominant_emotion']}"
    
    # Test case 3: Disgust
    result = emotion_detector("I feel disgusted just hearing about this")
    assert result['dominant_emotion'] == 'disgust', f"Expected 'disgust', got {result['dominant_emotion']}"
    
    # Test case 4: Sadness
    result = emotion_detector("I am so sad about this")
    assert result['dominant_emotion'] == 'sadness', f"Expected 'sadness', got {result['dominant_emotion']}"
    
    # Test case 5: Fear
    result = emotion_detector("I am really afraid that this will happen")
    assert result['dominant_emotion'] == 'fear', f"Expected 'fear', got {result['dominant_emotion']}"
    
    print("All unit tests passed!")


if __name__ == "__main__":
    test_emotion_detector()
