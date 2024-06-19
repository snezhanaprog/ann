document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('#form-record');
  const form_com = document.querySelector('#form-comment');

  form.addEventListener('submit', function(event) {
      event.preventDefault();

      const formData = new FormData(form);

      fetch('/submit_form', {
          method: 'POST',
          body: formData
      })
      .then(response => response.text())
      .then(data => {
          alert('Форма успешно отправлена!');
          console.log(data);
      })
      .catch(error => {
          console.error('Ошибка:', error);
          alert('Произошла ошибка при отправке формы.');
      });
  });

    form_com.addEventListener('submit', function(event) {
      event.preventDefault();

      const formData = new FormData(form_com);

      fetch('/submit_form-comment', {
          method: 'POST',
          body: formData
      })
      .then(response => response.text())
      .then(data => {
          alert('Форма успешно отправлена!');
          console.log(data);
      })
      .catch(error => {
          console.error('Ошибка:', error);
          alert('Произошла ошибка при отправке формы.');
      });
  });


});
