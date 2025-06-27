from nicegui.testing import User
from nicegui import ui

async def test_counter_initial_state(user: User) -> None:
    """Test that counter starts at 0 for new users."""
    await user.open('/')
    
    # Should see the counter app title
    await user.should_see('Counter App')
    
    # Should see initial count of 0
    await user.should_see('0')

async def test_counter_increment(user: User) -> None:
    """Test incrementing the counter."""
    await user.open('/')
    
    # Click increment button 3 times
    for i in range(1, 4):
        user.find(marker='increment-btn').click()
        await user.should_see(str(i))

async def test_counter_decrement(user: User) -> None:
    """Test decrementing the counter."""
    await user.open('/')
    
    # First increment to 2
    user.find(marker='increment-btn').click()
    user.find(marker='increment-btn').click()
    await user.should_see('2')
    
    # Click decrement once
    user.find(marker='decrement-btn').click()
    await user.should_see('1')
    
    # Click decrement again to go to 0
    user.find(marker='decrement-btn').click()
    await user.should_see('0')
    
    # Click decrement again to go negative
    user.find(marker='decrement-btn').click()
    await user.should_see('-1')

async def test_counter_reset(user: User) -> None:
    """Test resetting the counter."""
    await user.open('/')
    
    # Increment counter to 5
    for _ in range(5):
        user.find(marker='increment-btn').click()
    
    # Verify count is 5
    await user.should_see('5')
    
    # Click reset button
    user.find(marker='reset-btn').click()
    await user.should_see('0')

async def test_counter_persistence(user: User) -> None:
    """Test that counter value persists in user storage."""
    await user.open('/')
    
    # Increment counter 3 times
    for _ in range(3):
        user.find(marker='increment-btn').click()
    
    # Verify count is 3
    await user.should_see('3')
    
    # Simulate page reload by opening again
    await user.open('/')
    
    # Count should still be 3 due to user storage
    await user.should_see('3')

async def test_all_buttons_present(user: User) -> None:
    """Test that all required buttons are present with correct labels."""
    await user.open('/')
    
    # Check all buttons exist with correct text
    await user.should_see('Decrement')
    await user.should_see('Reset')
    await user.should_see('Increment')

async def test_counter_mixed_operations(user: User) -> None:
    """Test a combination of increment, decrement, and reset operations."""
    await user.open('/')
    
    # Start at 0
    await user.should_see('0')
    
    # Increment to 3
    for _ in range(3):
        user.find(marker='increment-btn').click()
    await user.should_see('3')
    
    # Decrement by 1
    user.find(marker='decrement-btn').click()
    await user.should_see('2')
    
    # Increment by 2
    for _ in range(2):
        user.find(marker='increment-btn').click()
    await user.should_see('4')
    
    # Reset to 0
    user.find(marker='reset-btn').click()
    await user.should_see('0')
    
    # Test going negative
    for _ in range(2):
        user.find(marker='decrement-btn').click()
    await user.should_see('-2')