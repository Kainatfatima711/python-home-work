import random, math

angle = random.randint(0, 360)
radian = math.radians(angle)

sin_val = math.sin(radian)
cos_val = math.cos(radian)
tan_val = math.tan(radian) if abs(cos_val) > 1e-10 else "undefined"

print(f"Angle: {angle}° ({radian:.4f} rad)")
print(f"sin({angle}°) = {sin_val:.4f}")
print(f"cos({angle}°) = {cos_val:.4f}")
print(f"tan({angle}°) = {tan_val if isinstance(tan_val, str) else format(tan_val, '.4f')}")