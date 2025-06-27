from nicegui import ui, app

def create():
    @ui.page('/')
    def page():
        # Get current count from user storage, default to 0
        current_count = app.storage.user.get('count', 0)
        
        # Create the count display label with prominent styling
        count_label = ui.label(str(current_count)).classes('text-6xl font-bold text-center').mark('count-display')
        
        def increment():
            app.storage.user['count'] = app.storage.user.get('count', 0) + 1
            count_label.set_text(str(app.storage.user['count']))
        
        def decrement():
            app.storage.user['count'] = app.storage.user.get('count', 0) - 1
            count_label.set_text(str(app.storage.user['count']))
        
        def reset():
            app.storage.user['count'] = 0
            count_label.set_text('0')
        
        # Layout the UI with proper spacing and alignment
        with ui.column().classes('items-center gap-8 p-8'):
            ui.label('Counter App').classes('text-3xl font-semibold mb-4')
            
            # Count display
            count_label
            
            # Button row
            with ui.row().classes('gap-4'):
                ui.button('Decrement', on_click=decrement, color='red').classes('text-lg px-6 py-3').mark('decrement-btn')
                ui.button('Reset', on_click=reset, color='grey').classes('text-lg px-6 py-3').mark('reset-btn')
                ui.button('Increment', on_click=increment, color='green').classes('text-lg px-6 py-3').mark('increment-btn')