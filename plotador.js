import {
  point,
  start,
  random_hsla,
  loop,
  random,
} from "../functionalModules.js";
const { sqrt, cos, sin, atan2, abs } = Math;

function init() {
  const [canvas, ctx] = start(
    document.querySelector("canvas"),
    window.innerWidth,
    window.innerHeight,
    {
      antialias: false,
    }
  );

  class Dot {
    constructor(pos, radius, angle) {
      this.x = pos.x;
      this.y = pos.y;

      this.radius = radius;
      this.color = random_hsla();
      this.vel = {
        x: random(-1, 1),
        y: random(-1, 1),
      };
      this.angle = angle;
    }

    draw() {
      point(ctx, this.x, this.y, this.radius, this.color, "FILL");
    }

    update() {
      let r = 1000
      this.x = canvas.width/2 + (cos(this.angle) * this.x + r);
      this.y = canvas.width/2 + (sin(this.angle) * this.y + r);
      this.angle += 10;
    }
  }

  let dots = [];
  let n = 200;
  let angle = (Math.PI * 2) / n;
  loop(n, (i) => {
    dots.push(new Dot({ x: random(0, 1), y: random(0, 1) }, 5, i * angle));
  })();

  function animate() {
    let animationRequest;
    (function animation() {
      animationRequest = requestAnimationFrame(animation);
      ctx.fillStyle = "rgba(0,0,0,.1)";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      for (let dot of dots) {
        dot.update();
        dot.draw();
      }
    })();
  }

  animate();
}

window.onload = init;
