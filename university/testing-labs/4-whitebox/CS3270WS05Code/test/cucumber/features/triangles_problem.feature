Feature: Triangle identification

Title: Student identifies triangle

Scenario: Equilateral
Given a triangle with sides of length 10, 10, 10
When the program identifies the triangle
Then the program should state 'Equilateral'

Scenario: Isosceles
Given a triangle with sides of length 10, 10, 15
When the program identifies the triangle
Then the program should state 'Isosceles'

Scenario: Scalene
Given a triangle with sides of length 5, 10, 14
When the program identifies the triangle
Then the program should state 'Scalene'

Scenario: Not a triangle
Given a triangle with sides of length 5, 10, 15
When the program identifies the triangle
Then the program should state 'Not a triangle'
