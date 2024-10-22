
import request from "supertest";
import app from "./index";
import {describe, expect, it, test} from '@jest/globals';
import express, { Express, Request, Response } from "express";

describe('GET /health', () => {
	it('should return a 200 status code', async () => {
		const response = await request(app)
			.get('/health');
		expect(response.statusCode).toBe(200);
    expect(response.text).toBe('✅ ok');
	});
});

describe('GET /', () => {
	it('should return a 200 status code', async () => {
		const response = await request(app)
			.get('/');
		expect(response.statusCode).toBe(200);
    expect(response.text).toBe('🍎 Hello! This is the Cymbal Superstore Inventory API.');
	});
});

describe('GET /newproducts', () => {
	it('should return a 200 status code and a list of 8 new products', async () => {
		const response = await request(app)
			.get('/newproducts');
		expect(response.statusCode).toBe(200);
    expect(response.body.length).toBe(8); 
	});
});

