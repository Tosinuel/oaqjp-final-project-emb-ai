"""
Emotion Detection module using Watson NLP library.
This module provides emotion detection functionality for analyzing text feedback.
"""
import json
import requests


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the given text using Watson NLP Emotion Predict function.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions.
        
    Returns:
        dict: A dictionary containing emotion scores and dominant emotion,
             or dictionary with None values if status code is 400.
    """
    # Watson NLP Emotion Predict API details
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Make the API request
    response = requests.post(url, headers=headers, json=input_json)
    
    # Check for status code 400 (bad request - blank entries)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Parse the response
    response_data = json.loads(response.text)
    
    # Extract emotions using dictionary syntax
    emotions = response_data['emotions']
    
    # Extract individual emotion scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find dominant emotion (highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
