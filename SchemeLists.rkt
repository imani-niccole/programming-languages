;; Progamming Languages | Scheme and Lists
;; Imani Candler | 10.30.2024
;; Objective: Create a list of 32 numbers. Print, sort, and reverse list. Find sum, average, largest, and smallest numbers.  

#lang racket
(display "Hi! Let's play with some lists!")
(newline)
(define mylist '(28 20 10 82 55 68 64 33 19 91 45 79 51 86 80 16 76 27 47 39 95 26 69 17 59 77 9 36 85 3 42 5))
(newline)
(display "Here's the created list: ")
(display mylist) ;; prints the list
(newline)
(newline)

;; SUM LIST
(display "Sum of the list: ")
(define (mysum mylist)
  (if (null? mylist) ;; if mylist is empty, print 0
      0
  (+ (car mylist) (mysum (cdr mylist))))) ;; otherwise, continue to add to the beginning of list
;; starts at beginning of list, adds to sum, then pushes everything forward
(mysum mylist) ;; calculates the sum of the list
(newline)

;; AVERAGE LIST
(display "Average of the list: ")
(/ (mysum mylist) 32) ;; calculates correct average, but prints out a fraction
(newline)

;; REVERSE LIST
(display "Reverse the list: ")
(define (reverse mylist)
  (if (null? mylist)
      mylist 
      (append (reverse (cdr mylist)) (list (car mylist)))))
(reverse mylist) 
(newline)

;; SORT LIST
(display "Sort list: ")
(sort mylist <) ;; sorts the list from smallest to largest number (uses sort function)
(newline)

;; SMALLEST NUMBER
(display "Smallest number of list: ")

(define (smallest lst) ;; searches thru mylist for smallest value
  (cond ;; very close to switch statement | checks conditions
    [(empty? lst) (empty)] ;; if list is empty, prints nothing
    [(empty? (rest lst)) (first lst)]
    [(> (first lst) (first (rest lst))) (smallest (rest lst))] ;; sign direction is important!!!!!
    [else (smallest (cons (first lst) (rest (rest lst))))])) ;; compares each value to each other
(smallest mylist) ;; displays smallest value in mylist

;; LARGEST NUMBER
(display "Largest number of list: ")

(define (largest lst)
  (cond ;; switch statement, checks conditions
    [(empty? lst) (empty)]
    [(empty? (rest lst)) (first lst)]
    [(< (first lst) (first (rest lst))) (largest (rest lst))] ;; sign direction is important!!!!!
    [else (largest (cons (first lst) (rest (rest lst))))])) ;; compares mylist values to each other

(largest mylist) ;; displays largest value in mylist
(newline)
(display "That's it! Till next time, goodbye!") 
   
