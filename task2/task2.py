import numpy as np
import unittest

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_department_average(threat_scores):
    return np.mean(threat_scores)

def calculate_weighted_average(department_averages, user_counts, importance_scores):
    total_weighted_score = 0
    total_weight = 0

    for avg, count, importance in zip(department_averages, user_counts, importance_scores):
        weight = count * importance
        total_weighted_score += avg * weight
        total_weight += weight

    return total_weighted_score / total_weight if total_weight != 0 else 0

def calculate_aggregated_threat_score(departments_data):
    department_averages = []
    user_counts = []
    importance_scores = []

    for department in departments_data:
        threat_scores = department['threat_scores']
        importance = department['importance']
        
        department_avg = calculate_department_average(threat_scores)
        
        department_averages.append(department_avg)
        user_counts.append(len(threat_scores))
        importance_scores.append(importance)
    
    return calculate_weighted_average(department_averages, user_counts, importance_scores)

class TestThreatScoreCalculator(unittest.TestCase):

    def test_department_average(self):
        # Test with known values to verify department average calculation
        scores = [10, 20, 30]
        self.assertAlmostEqual(calculate_department_average(scores), 20.0)

    def test_weighted_average(self):
        # Test known values to verify weighted average calculation
        averages = [10, 30, 50]
        user_counts = [10, 20, 30]
        importance_scores = [1, 2, 3]
        self.assertAlmostEqual(calculate_weighted_average(averages, user_counts, importance_scores), 36.67, places=2)

    def test_functional_case_equal_importance_similar_scores(self):
        # Case where all departments have similar threat scores and equal importance
        departments_data = [
            {'threat_scores': generate_random_data(40, 5, 50), 'importance': 3},
            {'threat_scores': generate_random_data(42, 5, 50), 'importance': 3},
            {'threat_scores': generate_random_data(38, 5, 50), 'importance': 3},
            {'threat_scores': generate_random_data(39, 5, 50), 'importance': 3},
            {'threat_scores': generate_random_data(41, 5, 50), 'importance': 3},
        ]
        score = calculate_aggregated_threat_score(departments_data)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 90)

    def test_functional_case_high_importance_high_threat(self):
        # Case where a single department with high importance has a high average threat score
        departments_data = [
            {'threat_scores': generate_random_data(10, 5, 50), 'importance': 1},
            {'threat_scores': generate_random_data(20, 5, 50), 'importance': 1},
            {'threat_scores': generate_random_data(85, 5, 50), 'importance': 5},
            {'threat_scores': generate_random_data(15, 5, 50), 'importance': 1},
            {'threat_scores': generate_random_data(25, 5, 50), 'importance': 1},
        ]
        score = calculate_aggregated_threat_score(departments_data)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 90)

    def test_functional_case_low_threat_high_importance(self):
        # Case where a low-threat department has a high importance score, while others are moderate
        departments_data = [
            {'threat_scores': generate_random_data(10, 5, 50), 'importance': 5},
            {'threat_scores': generate_random_data(40, 5, 50), 'importance': 1},
            {'threat_scores': generate_random_data(45, 5, 50), 'importance': 1},
            {'threat_scores': generate_random_data(42, 5, 50), 'importance': 1},
            {'threat_scores': generate_random_data(38, 5, 50), 'importance': 1},
        ]
        score = calculate_aggregated_threat_score(departments_data)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 90)

    def test_functional_case_mixed_scenario(self):
        # Mixed scenario with varying importance and threat levels across departments
        departments_data = [
            {'threat_scores': generate_random_data(60, 10, 100), 'importance': 3},
            {'threat_scores': generate_random_data(20, 5, 200), 'importance': 2},
            {'threat_scores': generate_random_data(40, 15, 150), 'importance': 4},
            {'threat_scores': generate_random_data(35, 10, 50), 'importance': 5},
            {'threat_scores': generate_random_data(25, 5, 75), 'importance': 1},
        ]
        score = calculate_aggregated_threat_score(departments_data)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 90)

if __name__ == '__main__':
    unittest.main()
