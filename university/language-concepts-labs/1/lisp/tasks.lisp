;; code for Task :
(print (+ 1 2))
;; the above expression throws an error

;; code for Task :
(format t "type something: ")
(setf input (read-line))
(if (not (string= input ""))
    (format t "you typed: ~a" input)
  (format t "you typed nothing"))

;; code for Task :
(let ((prg '(+ 1 n))) (progn (setf n 1) (format t "~d" (eval prg))))
;; The above Lisp expression first defines a very simple program,
;; and then prints the program.
