import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkGfm from 'remark-gfm';
import remarkRehype from 'remark-rehype';
import rehypeStringify from 'rehype-stringify';
import rehypeSlug from 'rehype-slug';

const CONTENT_DIR = path.join(process.cwd(), '../');

export interface ModuleInfo {
  id: string;
  title: string;
}

export interface DocumentInfo {
  slug: string;
  title: string;
  moduleId: string;
}

const MODULE_ZH_MAP: Record<string, string> = {
  '00-guides-and-trends': '指南与趋势',
  '01-foundation-models': '基础大模型',
  '02-infrastructure': '基础设施',
  '03-data-and-knowledge': '数据与知识',
  '04-dev-frameworks': '开发框架',
  '05-lowcode-platforms': '低代码平台',
  '06-tools-and-protocols': '工具与协议',
  '07-skills-and-plugins': '技能与插件',
  '08-observability': '可观测性',
  '09-safety-and-compliance': '安全与合规',
  '10-applications': '应用与场景',
};

export function getModules(locale: string = 'zh'): ModuleInfo[] {
  const entries = fs.readdirSync(CONTENT_DIR, { withFileTypes: true });
  const modules = entries
    .filter(entry => entry.isDirectory() && /^\d{2}-/.test(entry.name))
    .map(entry => {
      let title = entry.name
        .replace(/^\d{2}-/, '')
        .split('-')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
        
      if (locale === 'zh' && MODULE_ZH_MAP[entry.name]) {
        title = MODULE_ZH_MAP[entry.name];
      }
        
      return {
        id: entry.name,
        title
      };
    });
  
  return modules.sort((a, b) => a.id.localeCompare(b.id));
}

export function getDocumentsInModule(moduleId: string, locale: string = 'zh'): DocumentInfo[] {
  const modulePath = path.join(CONTENT_DIR, moduleId);
  if (!fs.existsSync(modulePath)) return [];
  
  const entries = fs.readdirSync(modulePath, { withFileTypes: true });
  
  const baseSlugs = new Set<string>();
  entries.forEach(e => {
    if (e.isFile() && e.name.endsWith('.md')) {
      const slug = e.name.replace(/\.en\.md$/, '').replace(/\.md$/, '');
      baseSlugs.add(slug);
    }
  });

  const docs = Array.from(baseSlugs).map(slug => {
    let fileName = `${slug}.md`;
    if (locale === 'en') {
      const enFileName = `${slug}.en.md`;
      if (fs.existsSync(path.join(modulePath, enFileName))) {
        fileName = enFileName;
      }
    }
    
    const filePath = path.join(modulePath, fileName);
    const fileContent = fs.readFileSync(filePath, 'utf8');
    
    const { data } = matter(fileContent);
    let title = data.title || slug;
    
    if (!data.title) {
      const h1Match = fileContent.match(/^#\s+(.+)$/m);
      if (h1Match) {
        title = h1Match[1].trim();
      }
    }
    
    return {
      slug,
      title,
      moduleId
    };
  });
    
  return docs;
}

export async function getDocumentContent(moduleId: string, slug: string, locale: string = 'zh') {
  let fileName = `${slug}.md`;
  let isFallback = false;
  
  if (locale === 'en') {
    const enFileName = `${slug}.en.md`;
    const enPath = path.join(CONTENT_DIR, moduleId, enFileName);
    if (fs.existsSync(enPath)) {
      fileName = enFileName;
    } else {
      isFallback = true;
    }
  }

  const filePath = path.join(CONTENT_DIR, moduleId, fileName);
  const fileContent = fs.readFileSync(filePath, 'utf8');
  const { data, content } = matter(fileContent);
  
  const processedContent = await unified()
    .use(remarkParse)
    .use(remarkGfm)
    .use(remarkRehype, { allowDangerousHtml: true })
    .use(rehypeSlug)
    .use(rehypeStringify, { allowDangerousHtml: true })
    .process(content);
    
  return {
    frontmatter: data,
    contentHtml: processedContent.toString(),
    isFallback
  };
}
