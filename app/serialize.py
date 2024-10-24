import json
import xml.etree.ElementTree
from typing import Any


class SerializeJSON:
    @staticmethod
    def serialize(book: Any) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXML:
    @staticmethod
    def serialize(book: Any) -> str:
        root = xml.etree.ElementTree.Element("book")
        title = xml.etree.ElementTree.SubElement(root, "title")
        title.text = book.title
        content = xml.etree.ElementTree.SubElement(root, "content")
        content.text = book.content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")


class Serialize:
    @staticmethod
    def serialize(book: Any, serialize_type: str) -> str:
        if serialize_type == "json":
            return SerializeJSON.serialize(book)
        elif serialize_type == "xml":
            return SerializeXML.serialize(book)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
