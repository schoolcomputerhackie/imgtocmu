from PIL import Image

image = Image.open("your_image.png")

canvas_width = 400
canvas_height = 400

rect_commands = []

scale_x = canvas_width / 20
scale_y = canvas_height / 20

for y in range(20):
    for x in range(20):
        pixel_color = image.getpixel((x, y))

        rect_x = x * scale_x
        rect_y = y * scale_y
        rect_width = scale_x
        rect_height = scale_y

        red, green, blue = pixel_color

        rect_command = f"Rect({int(rect_x)}, {int(rect_y)}, {int(rect_width)}, {int(rect_height)}, fill=rgb({red}, {green}, {blue}))"
        rect_commands.append(rect_command)

with open("commands.txt", "w") as file:
    for command in rect_commands:
        file.write(command + "\n")
