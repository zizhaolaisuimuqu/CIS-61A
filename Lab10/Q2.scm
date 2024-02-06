;way1
(define (filter-lst f lst)
  (cond ((null? lst) '())
        ((f (car lst)) 
            (cons (car lst)
            (filter-lst f (cdr lst))
            ))
        (else
         (filter-lst f (cdr lst))))
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)





;way2
(define (filter-lst f lst)
  (filter f lst)
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)