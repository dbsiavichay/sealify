"""from decimal import Decimal

from app.catalog.domain.entities import Product, ProductCreate
from app.catalog.domain.repositories import ProductRepository
from app.catalog.infra.adapters import ProductAdapter
from app.shared.domain.ports import EmailPort
from app.user.domain.entities import User


class TestProductAdapter:
    def test_create_product_success(self, mocker):
        # Arrange
        product_repository_mock = mocker.Mock(spec=ProductRepository)
        email_port_mock = mocker.Mock(spec=EmailPort)
        product_adapter = ProductAdapter(
            product_repository=product_repository_mock, email_port=email_port_mock
        )
        product = ProductCreate(
            sku="12345", name="Test Product", price=Decimal("10.00"), brand="Test Brand"
        )

        # Act
        product_adapter.create(product)

        # Assert
        product_repository_mock.create.assert_called_once_with(product)

    def test_retrieve_product_with_valid_sku_and_anonymous_user(self, mocker):
        # Arrange
        product_data = Product(
            sku="valid_sku",
            name="Test Product",
            price=10.99,
            brand="TestBrand",
            queried_by_anonymous=0,
        )
        mock_product_repository = mocker.Mock(spec=ProductRepository)
        mock_product_repository.retrieve.return_value = product_data
        mock_email_port = mocker.Mock(spec=EmailPort)

        product_adapter = ProductAdapter(mock_product_repository, mock_email_port)

        # Act
        result = product_adapter.retrieve(sku="valid_sku", user=None)
        print(result)

        # Assert
        mock_product_repository.retrieve.assert_called_once_with(sku="valid_sku")
        mock_product_repository.update_queried.assert_called_once_with("valid_sku", 1)
        assert result.queried_by_anonymous == 1

    def test_retrieve_product_with_valid_sku_and_user(self, mocker):
        # Arrange
        product_data = Product(
            sku="valid_sku",
            name="Test Product",
            price=10.99,
            brand="TestBrand",
            queried_by_anonymous=0,
        )
        mock_product_repository = mocker.Mock(spec=ProductRepository)
        mock_product_repository.retrieve.return_value = product_data
        mock_email_port = mocker.Mock(spec=EmailPort)

        product_adapter = ProductAdapter(mock_product_repository, mock_email_port)

        # Act
        result = product_adapter.retrieve(
            sku="valid_sku", user=User(email="test@test.com", hashed_password="")
        )
        print(result)

        # Assert
        mock_product_repository.retrieve.assert_called_once_with(sku="valid_sku")
        mock_product_repository.update_queried.assert_not_called()
        assert result.queried_by_anonymous == 0"""
