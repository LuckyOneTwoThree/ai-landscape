import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const DATA_DIR = path.join(process.cwd(), '../data');

export interface Tool {
  name: string;
  description?: string;
  description_en?: string;
  url?: string;
  repo?: string;
  category?: string;
  sub_category?: string;
  language?: string;
  license?: string;
  status?: string;
  tags?: string[];
  highlights?: string[];
  stars?: number;
  type?: string;
  // added internal field to generate unique slug
  slug: string;
}

export function getAllTools(): Tool[] {
  if (!fs.existsSync(DATA_DIR)) {
    return [];
  }

  const files = fs.readdirSync(DATA_DIR).filter(file => file.endsWith('.yaml'));
  const allTools: Tool[] = [];

  for (const file of files) {
    // Skip taxonomy.yaml as it's not a list of tools
    if (file === 'taxonomy.yaml') continue;

    const filePath = path.join(DATA_DIR, file);
    const fileContent = fs.readFileSync(filePath, 'utf8');
    
    try {
      const data = yaml.load(fileContent) as any[];
      if (Array.isArray(data)) {
        data.forEach(item => {
          if (item && item.name) {
            // Generate a slug from name (support Chinese and fallback to base64 if empty)
            let slug = item.name.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-\u4e00-\u9fa5]/g, '');
            if (!slug) {
              slug = Buffer.from(item.name).toString('base64').replace(/[^a-zA-Z0-9]/g, '').substring(0, 8).toLowerCase();
            }
            allTools.push({
              ...item,
              slug
            });
          }
        });
      }
    } catch (e) {
      console.error(`Error parsing ${file}:`, e);
    }
  }

  // Remove duplicates based on slug
  const uniqueTools = new Map<string, Tool>();
  allTools.forEach(tool => {
    if (!uniqueTools.has(tool.slug)) {
      uniqueTools.set(tool.slug, tool);
    }
  });

  return Array.from(uniqueTools.values());
}

export function getToolBySlug(slug: string): Tool | undefined {
  const allTools = getAllTools();
  return allTools.find(tool => tool.slug === slug);
}

export function getCategories(): string[] {
  const allTools = getAllTools();
  const categories = new Set<string>();
  allTools.forEach(tool => {
    if (tool.category) {
      categories.add(tool.category);
    }
  });
  return Array.from(categories);
}

export function getTags(): string[] {
  const allTools = getAllTools();
  const tags = new Set<string>();
  allTools.forEach(tool => {
    if (tool.tags && Array.isArray(tool.tags)) {
      tool.tags.forEach(tag => tags.add(tag));
    }
  });
  return Array.from(tags).sort();
}
