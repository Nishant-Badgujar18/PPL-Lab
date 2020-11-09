(format t "Enter the length of the list : ")
(defvar m (read))

(defvar l '())

(format t "Enter the elements of the list ~%")
(loop for x from 1 to m
      do (push (read) l)
)

(setq l (reverse l))

(format t "The list that you have entered is ~a ~%" l)

(format t "Enter which element of list you want to access : ")
(defvar n (read))

(loop for x from 1 to (- n 1)
      do (setq l (cdr l))
)

(format t "The ~a element of list is ~a" n (car l))
