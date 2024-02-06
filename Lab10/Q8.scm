(define (substitute s old new)
    (cond
        ((null? s) '())
        ((pair? s)
            (cons 
            (substitute (car s) old new)
            (substitute (cdr s) old new)))
        ((equal? s old) new)
        (else s)))