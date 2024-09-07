# soca_analysis.py

import numpy as np
from scipy import stats

def calculate_percentile(score, mean=0.5, std_dev=0.15):
    return stats.norm.cdf(score, mean, std_dev) * 100

def generate_soca_analysis(processed_data):
    # Define weights for each category
    weights = {
        "subject_knowledge": 0.3,
        "time_management": 0.2,
        "problem_solving": 0.2,
        "stress_management": 0.15,
        "study_techniques": 0.15
    }
    
    # Calculate weighted scores
    weighted_scores = {k: v * weights[k] for k, v in processed_data.items()}
    overall_score = sum(weighted_scores.values()) / sum(weights.values())
    
    # Calculate percentiles
    percentiles = {k: calculate_percentile(v) for k, v in processed_data.items()}
    overall_percentile = calculate_percentile(overall_score)
    
    # Determine strengths, opportunities, and challenges
    strengths = [k for k, v in percentiles.items() if v >= 70]
    opportunities = [k for k, v in percentiles.items() if 40 <= v < 70]
    challenges = [k for k, v in percentiles.items() if v < 40]
    
    # Generate analysis
    analysis = "SOCA Analysis:\n\n"
    analysis += f"Overall Performance: {overall_score:.2f} (Percentile: {overall_percentile:.1f})\n\n"
    
    analysis += "Strengths:\n"
    for strength in strengths:
        analysis += f"- {strength.replace('_', ' ').title()}: {processed_data[strength]:.2f} (Percentile: {percentiles[strength]:.1f})\n"
        analysis += "  " + get_strength_description(strength) + "\n"
    
    analysis += "\nOpportunities:\n"
    for opportunity in opportunities:
        analysis += f"- {opportunity.replace('_', ' ').title()}: {processed_data[opportunity]:.2f} (Percentile: {percentiles[opportunity]:.1f})\n"
        analysis += "  " + get_opportunity_description(opportunity) + "\n"
    
    analysis += "\nChallenges:\n"
    for challenge in challenges:
        analysis += f"- {challenge.replace('_', ' ').title()}: {processed_data[challenge]:.2f} (Percentile: {percentiles[challenge]:.1f})\n"
        analysis += "  " + get_challenge_description(challenge) + "\n"
    
    analysis += "\nAction Plan:\n"
    action_plan = generate_action_plan(strengths, opportunities, challenges, processed_data)
    for i, action in enumerate(action_plan, 1):
        analysis += f"{i}. {action}\n"
    
    return analysis

def get_strength_description(strength):
    descriptions = {
        "subject_knowledge": "You have a strong grasp of core JEE subjects. Keep refining your knowledge.",
        "time_management": "Your time management skills are excellent. This will be crucial during the exam.",
        "problem_solving": "You exhibit strong problem-solving abilities, a key skill for JEE success.",
        "stress_management": "You handle stress well, which is vital for maintaining performance under pressure.",
        "study_techniques": "Your study techniques are effective, helping you learn and retain information efficiently."
    }
    return descriptions.get(strength, "This is a notable strength in your JEE preparation.")

def get_opportunity_description(opportunity):
    descriptions = {
        "subject_knowledge": "There's room to deepen your understanding of JEE subjects.",
        "time_management": "Improving your time management could boost your overall performance.",
        "problem_solving": "Enhancing your problem-solving skills could significantly impact your JEE score.",
        "stress_management": "Better stress management techniques could help you perform more consistently.",
        "study_techniques": "Refining your study techniques could lead to more effective learning."
    }
    return descriptions.get(opportunity, "This area has potential for improvement in your JEE preparation.")

def get_challenge_description(challenge):
    descriptions = {
        "subject_knowledge": "Strengthening your subject knowledge should be a primary focus.",
        "time_management": "Developing better time management skills is crucial for your JEE success.",
        "problem_solving": "Improving your problem-solving approach is essential for tackling JEE questions.",
        "stress_management": "Learning to manage stress effectively will be important for your performance.",
        "study_techniques": "Adopting more effective study techniques could significantly enhance your preparation."
    }
    return descriptions.get(challenge, "This area needs significant attention in your JEE preparation.")

def generate_action_plan(strengths, opportunities, challenges, scores):
    action_plan = []
    
    if "subject_knowledge" in challenges:
        action_plan.append("Focus on intensive subject study. Identify weak areas and use targeted resources to improve.")
    elif "subject_knowledge" in opportunities:
        action_plan.append("Deepen your subject knowledge. Review advanced topics and solve complex problems.")
    
    if "time_management" in challenges or "time_management" in opportunities:
        action_plan.append("Develop a structured study schedule. Practice time-bound mock tests regularly.")
    
    if "problem_solving" in challenges:
        action_plan.append("Enhance problem-solving skills through daily practice. Focus on a variety of question types.")
    elif "problem_solving" in opportunities:
        action_plan.append("Refine problem-solving techniques. Tackle more challenging and diverse problems.")
    
    if "stress_management" in challenges:
        action_plan.append("Learn and apply stress management techniques like meditation, deep breathing, or yoga.")
    elif "stress_management" in opportunities:
        action_plan.append("Incorporate regular relaxation practices into your routine to optimize stress management.")
    
    if "study_techniques" in challenges or "study_techniques" in opportunities:
        action_plan.append("Explore and adopt diverse study resources. Consider techniques like spaced repetition or active recall.")
    
    if len(strengths) > 0:
        strongest = max(strengths, key=lambda x: scores[x])
        action_plan.append(f"Leverage your strength in {strongest.replace('_', ' ')} to support improvement in other areas.")
    
    return action_plan

# Example usage
if __name__ == "__main__":
    sample_data = {
        "subject_knowledge": 0.75,
        "time_management": 0.6,
        "problem_solving": 0.8,
        "stress_management": 0.5,
        "study_techniques": 0.7
    }
    print(generate_soca_analysis(sample_data))