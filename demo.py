"""Small fictional project for exploring Graphify code relationships."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    name: str
    price: int


@dataclass(frozen=True)
class OrderLine:
    product: Product
    quantity: int

    def subtotal(self) -> int:
        return self.product.price * self.quantity


def order_total(lines: list[OrderLine]) -> int:
    return sum(line.subtotal() for line in lines)


def format_receipt(lines: list[OrderLine]) -> str:
    total = order_total(lines)
    return f"Demo order total: {total}"


def main() -> None:
    sample = Product(name="Sample item", price=100)
    lines = [OrderLine(product=sample, quantity=2)]
    print(format_receipt(lines))


if __name__ == "__main__":
    main()
