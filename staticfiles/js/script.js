var slideIndex = 0;
showSlide(slideIndex);

function changeSlide(n) {
  showSlide(slideIndex += n);
}

function showSlide(n) {
  var slides = document.getElementsByClassName("slide");
  if (n >= slides.length) {
    slideIndex = 0;
  } else if (n < 0) {
    slideIndex = slides.length - 1;
  }

  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  
  slides[slideIndex].style.display = "block";
}

<script>
document.addEventListener("DOMContentLoaded", function() {
    const roomCapacitySelect = document.getElementById("id_room_capacity");
    const roomPricingSelect = document.getElementById("id_room_pricing");

    const roomPricingMap = {
        {% for room_id, room_name, room_pricing in room_choices %}
            {{ room_id }}: {{ room_pricing }},
        {% endfor %}
    };

    roomCapacitySelect.addEventListener("change", function() {
        const selectedRoomId = parseInt(roomCapacitySelect.value);
        const pricing = roomPricingMap[selectedRoomId];
        roomPricingSelect.value = pricing;
    });

    // Trigger change event on page load (if a room is already selected)
    roomCapacitySelect.dispatchEvent(new Event("change"));
});
</script>

