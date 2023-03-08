(defun gps-line()
"Print the current buffer line number out of the total lines in the buffer"
  (interactive)
  (let ((start (point-min))
	(end (point-max))
	(n (line-number-at-pos))
	(total (count-lines (point-min) (point-max))))

    (if (= start 1)
	(if (= start end)
	    (message "Line 1/0")
	    (if (string= (buffer-substring-no-properties (- end 1) end) "\n")
	        (message "Line %d/%d" n total)
	        (message "Line %d/%d" n (- total 1))))
      (save-excursion
        (save-restriction
          (widen)
          (message "line %d (narrowed line %d)"
                   (+ n (line-number-at-pos start) -1) n))))))
