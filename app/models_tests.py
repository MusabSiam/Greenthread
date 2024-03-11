from django.test import TestCase
from django.utils import timezone
from app.models import User, ClothingItem, Message, Category, Review


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        User.objects.create(username='testuser', password='12345')

    def test_user_creation(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username, 'testuser')

class ClothingItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a User for foreign key relationship
        testuser = User.objects.create(username='testuser', password='12345')
        ClothingItem.objects.create(owner=testuser, description='Green Shirt', size='M', category='Shirt')

    def test_clothing_item_creation(self):
        item = ClothingItem.objects.get(id=1)
        self.assertEqual(item.description, 'Green Shirt')

class MessageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        sender = User.objects.create(username='sender', password='12345')
        recipient = User.objects.create(username='recipient', password='12345')
        item = ClothingItem.objects.create(owner=recipient, description='Blue Jeans', size='L', category='Jeans')
        Message.objects.create(sender=sender, recipient=recipient, item=item, content='Do you still have these?')

    def test_message_creation(self):
        message = Message.objects.get(id=1)
        self.assertEqual(message.content, 'Do you still have these?')

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Category instance for testing
        Category.objects.create(name='T-Shirts')

    def test_category_str_method(self):
        category = Category.objects.get(id=1)
        expected_object_name = category.name
        self.assertEqual(str(category), expected_object_name)

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create User and ClothingItem instances
        user = User.objects.create(username='reviewer', password='12345')
        item_owner = User.objects.create(username='item_owner', password='12345')
        item = ClothingItem.objects.create(owner=item_owner, description='Stylish Hat', size='One Size', category='Hat')
        # Create a Review instance
        Review.objects.create(item=item, reviewer=user, rating=5, comment='Great quality!')

    def test_review_content(self):
        review = Review.objects.get(id=1)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, 'Great quality!')

