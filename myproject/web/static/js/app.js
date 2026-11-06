      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateCount(entry.target);
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.6 }
    );
    counters.forEach((el) => io.observe(el));
  } else {
    counters.forEach(animateCount);
  }
  const path = document.getElementById("route-path");
  const dot = document.getElementById("bike-dot");
  if (path && dot && path.getTotalLength) {
    const length = path.getTotalLength();
    let t = 0;
    const loop = () => {
      t = (t + 0.35) % 100;
      const pt = path.getPointAtLength((t / 100) * length);
      dot.setAttribute("cx", String(pt.x));
      dot.setAttribute("cy", String(pt.y));
      requestAnimationFrame(loop);
    };
    loop();
  }
  const csrf = document.querySelector("[name=csrfmiddlewaretoken]")?.value;
  const quoteForm = document.getElementById("quote-form");
  const quoteMsg = document.getElementById("quote-msg");
  quoteForm?.addEventListener("submit", async (event) => {
    event.preventDefault();
    quoteMsg.classList.remove("hidden", "text-red-600", "text-emerald-600");
    const body = new FormData(quoteForm);
    const res = await fetch(quoteForm.action, {
      method: "POST",
      headers: { "X-CSRFToken": csrf, "X-Requested-With": "XMLHttpRequest" },
      body,
    });
    const data = await res.json();
    if (data.ok) {
      quoteMsg.classList.add("text-emerald-600");
      quoteMsg.textContent = data.message;
      quoteForm.reset();
    } else {
      quoteMsg.classList.add("text-red-600");
      const first = data.errors ? Object.values(data.errors)[0][0] : "Please check the form.";
      quoteMsg.textContent = first;
    }
    quoteMsg.classList.remove("hidden");
  });
  const statusOrder = ["booked", "picked", "in_transit", "ofd", "delivered"];
  const trackForm = document.getElementById("track-form");
  const trackResult = document.getElementById("track-result");
  const progressBar = document.getElementById("progress-bar");
  const steps = document.querySelectorAll("#track-steps li");
  document.getElementById("fill-demo")?.addEventListener("click", () => {
    const input = document.getElementById("track-id");
    if (input) input.value = "MOT-48291";
  });
  const paintTrack = (data) => {
    trackResult.classList.remove("hidden");
    trackResult.innerHTML = `
      <p class="text-xs text-slate-500">${data.tracking_id} · ${data.insured ? "Insured" : "Uninsured"}</p>
      <p class="mt-1 text-lg font-semibold text-white">${data.bike_model}</p>
      <p class="text-sm text-slate-400">${data.origin} → ${data.destination}</p>
      <p class="mt-3 text-ember-400">${data.status} · last hub ${data.last_hub} · ETA ${data.eta_hours}h</p>
    `;
    progressBar.style.width = `${data.progress}%`;
    const idx = statusOrder.indexOf(data.status_key);
    steps.forEach((li, i) => {
      li.classList.toggle("text-slate-500", i > idx);
      li.classList.toggle("text-white", i <= idx);
      const dotEl = li.querySelector("span");
      if (dotEl) {
        dotEl.className =
          "mt-1 h-2 w-2 rounded-full " + (i <= idx ? "bg-ember-500" : "bg-white/20");
      }
    });
  };
  trackForm?.addEventListener("submit", async (event) => {
    event.preventDefault();
    const id = document.getElementById("track-id").value.trim();
    const res = await fetch(`/track/?id=${encodeURIComponent(id)}`);
    const data = await res.json();
    if (!data.ok) {
      trackResult.classList.remove("hidden");
      trackResult.innerHTML = `<p class="text-rose-300">${data.message}</p>`;
      return;
    }
    paintTrack(data);
  });
})();
