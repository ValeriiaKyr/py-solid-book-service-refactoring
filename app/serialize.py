import json
import xml.etree.ElementTree as ET


class SerializeJSON:
    @staticmethod
    def serialize(book):
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXML:
    @staticmethod
    def serialize(book):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class Serialize:
    @staticmethod
    def serialize(book, serialize_type: str):
        if serialize_type == "json":
            return SerializeJSON.serialize(book)
        elif serialize_type == "xml":
            return SerializeXML.serialize(book)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
