# q1
feature1 = 3;
feature2 = 7;
last_digit_of_mob_no = 1;
first_digit_of_mob_no = 6;
weight1 = 0.1*last_digit_of_mob_no;
weight2 = 0.3*first_digit_of_mob_no;

final_score = (feature1*weight1) + (feature2*weight2);
print("Final score is: ", final_score);