(define (over-or-under x y)
    (cond
	    ((> x y) 1)
	    ((< x y) -1)
        ((= x y) 0))
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0
