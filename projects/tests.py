from django.test import TestCase
from projects.models import Project, Rating, Label
from django.contrib.auth.models import User
# Create your tests here.


class TestProject(TestCase):
    """Test Project model class"""

    def setUp(self):
        """Set up model instances"""
        self.user = User.objects.create(
            username="brian", password1="pass1123", password2="pass1123")
        self.project = Project.objects.create(
            name="Test Project", user=self.user, description="Project description test",)

    def tearDown(self):
        """Reset model instances after every test"""
        User.objects.all().delete()
        Project.objects.all().delete()


class TestLabel(TestCase):
    """Test Label model class"""

    def setUp(self):
        """Set up model instances"""
        self.user = User.objects.create(
            username="brian",  password="pass1123")
        self.project = Project.objects.create(
            name="Test Project", user=self.user, description="Project description test",)

        self.labels = ["design", "python", "webdev", "django", "angular"]

    def tearDown(self):
        """Reset model instances after every test"""
        User.objects.all().delete()
        Project.objects.all().delete()
        Label.objects.all().delete()

    def test_create_label(self):
        """Test creating a label"""
        for name in self.labels:
            label = Label(name=name)
            self.project.labels.add(Label.save_label(label))
        labels = Label.objects.all()
        project_labels = self.project.labels.all()
        self.assertEqual(len(project_labels), 5)
        self.assertEqual(len(labels), len(self.labels))  # should be 5

    def test_avoid_label_duplicates(self):
        """Test avoid creating duplicate labels"""
        new_label = Label(name=self.labels[0])
        Label.save_label(new_label)
        duplicate = Label(name=self.labels[0])
        Label.save_label(duplicate)
        labels = Label.objects.all()
        self.assertTrue(len(labels), 1)  # should be 1
