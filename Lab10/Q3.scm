(define (make-adder num)

    (lambda (x) (+ x num))

)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13
