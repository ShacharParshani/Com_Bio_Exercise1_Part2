import pygame

class InputTextBox:
    def __init__(self, title, input_box):
        self.title = title
        self.input_box = input_box
        self.input_text = ""
        self.cursor_pos = 0
    def GetPos(self, event, font, screen):
        if event.key == pygame.K_BACKSPACE:
            self.input_text = self.input_text[:-1]
            # Delete the character to the left of the cursor
            if self.cursor_pos > 0:
                self.input_text = self.input_text[:self.cursor_pos - 1] + self.input_text[self.cursor_pos:]
                self.cursor_pos -= 1
        elif event.key == pygame.K_DELETE:
            # Delete the character to the right of the cursor
            if self.cursor_pos < len(self.input_text):
                input_text = self.input_text[:self.cursor_pos] + self.input_text[self.cursor_pos + 1:]
        elif event.key == pygame.K_LEFT:
            # Move the cursor left
            if self.cursor_pos > 0:
                self.cursor_pos -= 1
        elif event.key == pygame.K_RIGHT:
            # Move the cursor right
            if self.cursor_pos < len(self.input_text):
                self.cursor_pos += 1
        elif event.unicode:
            # Insert the typed character at the cursor position
            self.input_text = self.input_text[:self.cursor_pos] + event.unicode + self.input_text[self.cursor_pos:]
            self.cursor_pos += 1

    def Draw(self, font, screen, title_locat):
        # Draw the title
        tab_text = font.render(self.title, True, (0, 0, 0))
        screen.blit(tab_text, title_locat)

        # Draw the input boxes
        pygame.draw.rect(screen, (0, 0, 0), self.input_box, 2)
        input_text_surface = font.render(self.input_text, True, (0, 0, 0))
        screen.blit(input_text_surface, (self.input_box.x + 3, self.input_box.y + 3))

        # Draw the mouse cursor
        cursor_pos_px = self.input_box.x + 5 + font.size(self.input_text[:self.cursor_pos])[0]
        cursor_y1 = self.input_box.y + 5
        cursor_y2 = cursor_y1 + font.size(self.input_text)[1]
        pygame.draw.line(screen, (0, 0, 0), (cursor_pos_px, cursor_y1), (cursor_pos_px, cursor_y2))

