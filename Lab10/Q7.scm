(define (no-repeats s)
  (cond
    ((null? s) '())
    ((not (null? (filter (lambda (y) (= (car s) y)) (cdr s)))) (no-repeats (cdr s)))
    (else (cons (car s) (no-repeats (cdr s))))
  ))


;;; Tests
(no-repeats (list 5 4 5 4 2 2))
; expect (5 4 2)