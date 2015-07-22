package com.teds.service;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.List;

import org.apache.poi.openxml4j.exceptions.InvalidFormatException;
import org.apache.poi.openxml4j.opc.OPCPackage;
import org.apache.poi.xwpf.usermodel.XWPFDocument;
import org.apache.poi.xwpf.usermodel.XWPFParagraph;
import org.apache.poi.xwpf.usermodel.XWPFRun;
import org.apache.poi.xwpf.usermodel.XWPFTable;
import org.apache.poi.xwpf.usermodel.XWPFTableCell;
import org.apache.poi.xwpf.usermodel.XWPFTableRow;

public class BulkDocChange {

	public static void main(String[] args) throws FileNotFoundException,
			IOException, InvalidFormatException {

		XWPFDocument teddoc = new XWPFDocument(
				OPCPackage.open("C:\\Java\\utest\\testtoread.docx"));
		for (XWPFParagraph p : teddoc.getParagraphs()) {
			List<XWPFRun> tedrn = p.getRuns();
			if (tedrn != null) {
				for (XWPFRun r : tedrn) {
					String searchtext = r.getText(0);
					if (searchtext != null && searchtext.contains("Mohan")) {
						searchtext = searchtext.replace("Mohan", "Geek");
						r.setText(searchtext, 0);
					}
				}
			}
		}
		for (XWPFTable tedtbl : teddoc.getTables()) {
			for (XWPFTableRow row : tedtbl.getRows()) {
				for (XWPFTableCell cell : row.getTableCells()) {
					for (XWPFParagraph p : cell.getParagraphs()) {
						for (XWPFRun r : p.getRuns()) {
							String searchtext = r.getText(0);
							if (searchtext.contains("Mohan")) {
								searchtext = searchtext.replace("Mohan", "Geek");
								r.setText(searchtext);
							}
						}
					}
				}
			}
		}
		teddoc.write(new FileOutputStream("C:\\Java\\utest\\new_testtoread.docx"));

	}
}
