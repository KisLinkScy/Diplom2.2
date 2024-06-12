      $(document).ready(function () {
        var monthNames = [
          "Январь",
          "Вевраль",
          "Март",
          "Апрель",
          "Май",
          "Июнь",
          "Июль",
          "Август",
          "Сернябрь",
          "Октябрь",
          "Ноябрь",
          "Декабрь",
        ];
        var dayNames = [
          "Воскресенье",
          "Понедельник",
          "Вторник",
          "Среда",
          "Четверг",
          "Пятница",
          "Суббота",
        ];
        var newDate = new Date();
        newDate.setDate(newDate.getDate());
        $("#Date").html(
          dayNames[newDate.getDay()] +
            " " +
            newDate.getDate() +
            " " +
            monthNames[newDate.getMonth()] +
            " " +
            newDate.getFullYear()
        );
        setInterval(function () {
          var seconds = new Date().getSeconds();
          $("#sec").html((seconds < 10 ? "0" : "") + seconds);
        }, 1000);
        setInterval(function () {
          var minutes = new Date().getMinutes();
          $("#min").html((minutes < 10 ? "0" : "") + minutes);
        }, 1000);
        setInterval(function () {
          var hours = new Date().getHours();
          $("#hours").html((hours < 10 ? "0" : "") + hours);
        }, 1000);

        $("#myclock").thooClock({
          dialColor: "#222",
          secondHandColor: "#C00",
          size: 300,
          showNumerals: false,
          brandText: "BootstrapTema",
          brandText2: "Plugin for website",
        });
      });
